import { createQueue } from "kue";

const queue = createQueue();

const object = {
  phoneNumber: '0903033811',
  message: 'push notification code message',
}

const job = queue.create('push_notification_code', object).save((err) => {
    if (!err) {
        console.log(`Notification job created: ${job.id}`);
    }
});

job.on('complete', () => console.log('Notification job completed'));

job.on('failed', () => console.log('Notification job failed'));
