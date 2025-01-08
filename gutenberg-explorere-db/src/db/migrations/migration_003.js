// Migration 003:
// Update readLater and downloaded columns to be nullable in UserBooks table
//

module.exports = {
    up: (queryInterface, Sequelize) => {
        return queryInterface.sequelize.transaction(t => 
            Promise.all([
                queryInterface.changeColumn('UserBooks', 'readLater', {
                    type: Sequelize.DataTypes.BOOLEAN,
                    allowNull: true
                }, { transaction: t }),
                queryInterface.changeColumn('UserBooks', 'downloaded', {
                    type: Sequelize.DataTypes.BOOLEAN,
                    allowNull: true
                }, { transaction: t })
            ])
        );
    },
    down: (queryInterface, Sequelize) => {
        return queryInterface.sequelize.transaction(t => 
            Promise.all([
                queryInterface.changeColumn('UserBooks', 'readLater', {
                    type: Sequelize.DataTypes.BOOLEAN,
                    allowNull: false
                }, { transaction: t }),
                queryInterface.changeColumn('UserBooks', 'downloaded', {
                    type: Sequelize.DataTypes.BOOLEAN,
                    allowNull: false
                }, { transaction: t })
            ])
        );
    },
};