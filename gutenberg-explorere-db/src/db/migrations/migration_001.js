// Migration 001:
// Initial setup of tables for gutenberg db
//

module.exports = {
    up: (queryInterface, Sequelize) => {
        return queryInterface.sequelize.transaction(t => 
            Promise.all([
                queryInterface.createTable('User', {
                    id: Sequelize.DataTypes.UUID,
                    firstName: Sequelize.DataTypes.STRING,
                    lastName: Sequelize.DataTypes.STRING,
                    email: Sequelize.DataTypes.STRING,
                    passwordHash: Sequelize.DataTypes.TEXT,
                    createdAt: Sequelize.DataTypes.DATE
                }, { transaction: t }),
                queryInterface.createTable('UserBooks', {
                    userId: Sequelize.DataTypes.UUID,
                    bookId: Sequelize.DataTypes.STRING,
                    readLater: Sequelize.DataTypes.BOOLEAN,
                    downloaded: Sequelize.DataTypes.BOOLEAN,
                    createdAt: Sequelize.DataTypes.DATE
                }, { transaction: t })
            ])
        );
    },
    down: (queryInterface, Sequelize) => {
        return queryInterface.sequelize.transaction(t => 
            Promise.all([
                queryInterface.dropTable('User', { transaction: t }),
                queryInterface.dropTable('UserBooks', { transaction: t })
            ])
        );
    },
};