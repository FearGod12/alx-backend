function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }

    for (let each of jobs) {
        const job = queue.create('push_notification_code_3', each);
        const jobId = job.id;
        
        job.save(err => {
            if (!err) {
                console.log(`Notification job created: ${jobId}`);
            }
        });
        job.on('complete', () => console.log(`Notification job ${jobId} completed`));

        job.on('failed', (err) => console.log(`Notification job ${jobId} failed: ${err}`));

        job.on('progress', (percent) => console.log(`Notification job ${jobId} ${percent}% complete`));
    }
}

module.exports = createPushNotificationsJobs;
