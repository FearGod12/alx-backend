import { createClient, print } from "redis";

const client = createClient()
client.on('connect', () => {
    console.log('Redis client connected to the server')
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
})


function setNewSchool(schoolName, value) {
    const reply = client.SET(schoolName, value, (err, value) => {
        print(`Reply: ${value}`);
    })
}

function displaySchoolValue(schoolName) {
    const reply = client.GET(schoolName, (err, reply) => {
        console.log(reply);
    })
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
