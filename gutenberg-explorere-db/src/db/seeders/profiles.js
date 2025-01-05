const { faker } = require('@faker-js/faker');

const defaultHashedPasswordWithSalt = "";

module.exports = {
    up: (queryInterface, Sequelize) => {
      const users = [];
      for (let i = 0; i < 20; i++){
        users.push({
          id: faker.string.uuid(),
          firstName: faker.person.firstName(),
          lastName: faker.person.lastName(),
          email: faker.internet.email(),
          passwordHash: defaultHashedPasswordWithSalt,
          createdAt: faker.date.recent
        });
      }
      return queryInterface.bulkInsert('Users', users);
    },
    down: (queryInterface, Sequelize) => {
      return queryInterface.bulkDelete('Users', null, {});
    },
  };