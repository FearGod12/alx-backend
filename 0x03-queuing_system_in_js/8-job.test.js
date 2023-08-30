import { expect } from "chai";
import createPushNotificationsJobs from "./8-job";

import { createQueue } from "kue";


describe('createPushNotificationsJobs', function () {
    const queue = createQueue();

    before(function () {
        queue.testMode.enter();
    });

    afterEach(function () {
        queue.testMode.clear();
    });

    after(function () {
        queue.testMode.exit();
    });


    it('validate which jobs are inside the queue', function () {

        const jobs = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account'
            },
            {
                phoneNumber: '4153518781',
                message: 'This is the code 4562 to verify your account'
            },
            {
                phoneNumber: '4153518743',
                message: 'This is the code 4321 to verify your account'
            },
            {
                phoneNumber: '4153538781',
                message: 'This is the code 4562 to verify your account'
            },
            {
                phoneNumber: '4153118782',
                message: 'This is the code 4321 to verify your account'
            },
            {
                phoneNumber: '4153718781',
                message: 'This is the code 4562 to verify your account'
            },
            {
                phoneNumber: '4159518782',
                message: 'This is the code 4321 to verify your account'
            },
            {
                phoneNumber: '4158718781',
                message: 'This is the code 4562 to verify your account'
            },
            {
                phoneNumber: '4153818782',
                message: 'This is the code 4321 to verify your account'
            },
            {
                phoneNumber: '4154318781',
                message: 'This is the code 4562 to verify your account'
            },
            {
                phoneNumber: '4151218782',
                message: 'This is the code 4321 to verify your account'
            }
        ];
        
        createPushNotificationsJobs(jobs, queue);
        expect(queue.testMode.jobs.length).to.equal(11);
        expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[10].data).to.deep.equal({
            phoneNumber: '4151218782',
            message: 'This is the code 4321 to verify your account'
        });
    });

    it('display an error message if jobs is  not an array', function () {
        const jobs = {
            phoneNumber: '4151218782',
            message: 'This is the code 4321 to verify your account'
        };

        expect(() => createPushNotificationsJobs(jobs, queue)).to.throw(Error, 'Jobs is not an array');
        expect(queue.testMode.jobs.length).to.equal(0);
    })
});
