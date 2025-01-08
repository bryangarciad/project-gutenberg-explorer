// Migration 002:
// Add Book model to store book metadata and content, pg will use toast compress to store content efficiently, 
// going with this instead of static file storage due to time constrains and simplicity
//

module.exports = {
    up: (queryInterface, Sequelize) => {
        return queryInterface.sequelize.transaction(t => 
            Promise.all([
                queryInterface.createTable('Book', {
                    id: Sequelize.DataTypes.UUID,
                    gutenbergId: {
                        type: Sequelize.DataTypes.STRING,
                        allowNull: true
                    },
                    coverUrl: {
                        type: Sequelize.DataTypes.STRING,
                        allowNull: true
                    },
                    author: {
                        type: Sequelize.DataTypes.STRING,
                        allowNull: true
                    },
                    original_publication: {
                        type: Sequelize.DataTypes.STRING,
                        allowNull: true
                    },
                    credits: {
                        type: Sequelize.DataTypes.STRING,
                        allowNull: true
                    },
                    language: {
                        type: Sequelize.DataTypes.STRING,
                        allowNull: true
                    },
                    category: {
                        type: Sequelize.DataTypes.STRING,
                        allowNull: true
                    },
                    release_date: {
                        type: Sequelize.DataTypes.DATE,
                        allowNull: true
                    },
                    copyright_status: {
                        type: Sequelize.DataTypes.STRING,
                        allowNull: true
                    },
                    content: {
                        type: Sequelize.DataTypes.TEXT,
                        allowNull: true
                    },
                    createdAt: Sequelize.DataTypes.DATE,
                }, { transaction: t }),
            ])
        );
    },
    down: (queryInterface, Sequelize) => {
        return queryInterface.sequelize.transaction(t => 
            Promise.all([
                queryInterface.dropTable('Book', { transaction: t }),
            ])
        );
    },
};