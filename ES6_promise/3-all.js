// In this file, import uploadPhoto and createUser from utils.js

import { createUser, uploadPhoto } from './utils';

export default function handleProfileSignup() {
  const photoPromise = uploadPhoto();
  const userPromise = createUser();

  return Promise.all([photoPromise, userPromise])
    .then((results) => {
      const photoResult = results[0];
      const userResult = results[1];

      const { body: photoBody } = photoResult;
      const { firstName, lastName } = userResult;

      console.log(`Foto: ${photoBody}, Usuario: ${firstName} ${lastName}`);
    })
    .catch(() => {
      console.log(('Signup system offline'));
    });
}
