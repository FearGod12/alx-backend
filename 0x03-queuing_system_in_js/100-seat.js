const express = require('express');
const { createQueue } = require('kue');
const redis = require('redis');
const { promisify } = require('util');

const client = redis.createClient();

const asyncGet = promisify(client.get).bind(client);

function reserveSeat(number) {
    client.set('available_seats', number);
}

async function getCurrentAvailableSeats() {
    return await asyncGet('available_seats')
}

const queue = createQueue();
const port = 1245;

const app = express();
let reservationEnabled = true;

app.get('/available_seats', async (req, res) => {
    const seats = await getCurrentAvailableSeats()
    res.json({ "numberOfAvailableSeats": seats });
});

app.get('/reserve_seat', (req, res) => {
    if (reservationEnabled === false) {
        res.json({ "status": "Reservation are blocked" });
    }
    const job = queue.create('reserve_seat').save(err => {
        if (err) {
            res.json({ "status": "Reservation failed" });
        } else {
            res.json({ "status": "Reservation in process" });
        }
    });

    job.on('complete', () => console.log(`Seat reservation job ${job.id} completed`));

    job.on('failed', (err) => console.log(`Seat reservation job ${job.id} failed: err`));
})

app.get('/process', (req, res) => {
    queue.process('reserve_seat', async (job, done) => {
        const seats = await getCurrentAvailableSeats();
        const new_seats = parseInt(seats) - 1;
        if (new_seats === 0) {
            reservationEnabled = false;
        }
        if (new_seats >= 0) {
            reserveSeat(new_seats);
            done();
        } else {
            done(new Error('Not enough seats available'));
        }
    });
    res.json({ "status": "Queue processing" });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
    reserveSeat(50);
});

module.exports = app;
