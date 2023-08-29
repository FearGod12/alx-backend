import { createClient, print } from "redis";
import { promisify } from 'util';

const client = createClient()
client.on('connect', () => {
    console.log('Redis client connected to the server')
});

client.on('Error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
})


function setNewSchool(schoolName, value) {
    client.SET(schoolName, value, (err, value) => {
        print(`Reply: ${value}`);
    })
}

const getAsync = promisify(client.GET).bind(client);

async function displaySchoolValue(schoolName) {
    const reply = await getAsync(schoolName);
    console.log(reply);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
