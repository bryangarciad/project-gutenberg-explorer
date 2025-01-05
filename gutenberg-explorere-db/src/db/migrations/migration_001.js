// Migration 001:
// Initial setup of tables for gutenberg db
//

module.exports = {
    up: (queryInterface, Sequelize) => {
        return queryInterface.createTable('Profiles', {
        name: Sequelize.DataTypes.STRING,
        isBetaMember: {
            type: Sequelize.DataTypes.BOOLEAN,
            defaultValue: false,
            allowNull: false,
        },
        });
    },
    down: (queryInterface, Sequelize) => {
        return queryInterface.dropTable('Profiles');
    },
};