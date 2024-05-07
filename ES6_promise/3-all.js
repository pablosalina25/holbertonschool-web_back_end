// In this file, import uploadPhoto and createUser from utils.js

import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then(([photoResponse, userResponse]) => {
      const { body: photoBody } = photoResponse;
      const { firstName, lastName } = userResponse;
      console.log(`${photoBody} ${firstName} ${lastName}`);
    })
    .catch(() => {
      console.log('The signup system offline');
    });
}
