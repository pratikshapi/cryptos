const Buzzcoin = artifacts.require("Buzzcoin");

module.exports = function(deployer) {
  deployer.deploy(Buzzcoin);
};

