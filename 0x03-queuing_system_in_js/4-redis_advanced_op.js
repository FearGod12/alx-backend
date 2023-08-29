import { createClient, print } from "redis";
import { promisify } from 'util';

const client = createClient()
client.on('connect', () => {
    console.log('Redis client connected to the server')
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
})
const items = {
    'Portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 20,
    'Cali': 40,
    'Paris': 2,
    }
    for (let item of Object.entries(items)) {
        client.hset('HolbertonSchools', item[0], item[1], (err, reply) => {
            if (err) print(err);
            else {
                print(reply);
            }
        });
    }

// for (let item of Object.entries(items)) {
//     client.hdel('HolbertonSchools', item[0], (err, reply) =>
//     {
//         print(reply);
//         })
//     }

client.hgetall('HolbertonSchools', (err, hashobject) => {
    if (err) console.log(err);
    else {
        console.log(hashobject);
    }
})
