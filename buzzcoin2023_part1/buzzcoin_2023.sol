pragma solidity >= 0.5.0 < 0.9.0;

/*
 ________  ___  ___  ________  ________  ________  ________  ___  ________      
|\   __  \|\  \|\  \|\_____  \|\_____  \|\   ____\|\   __  \|\  \|\   ___  \    
\ \  \|\ /\ \  \\\  \\|___/  /|\|___/  /\ \  \___|\ \  \|\  \ \  \ \  \\ \  \   
 \ \   __  \ \  \\\  \   /  / /    /  / /\ \  \    \ \  \\\  \ \  \ \  \\ \  \  
  \ \  \|\  \ \  \\\  \ /  /_/__  /  /_/__\ \  \____\ \  \\\  \ \  \ \  \\ \  \ 
   \ \_______\ \_______\\________\\________\ \_______\ \_______\ \__\ \__\\ \__\
    \|_______|\|_______|\|_______|\|_______|\|_______|\|_______|\|__|\|__| \|__|
*/

contract Buzzcoin {
    mapping (address => bool) private p1;
    mapping (address => bool) private p2;
    mapping (address => bool) private p3;
    mapping (address => bool) private p4;
    mapping (address => bool) private p5;

    mapping (address => bool) private perm;
    address[95] private users;
    address owner;
    function () external payable {}
    function donate() external payable {}
    uint public mask;
    uint public logmask;
    constructor() public{
        owner = msg.sender;
        users = [0x1421350ab6660421d2EA4e423a52030c9A19010E,
0x3bd084E44F896C08bb988216cDf5f6B10cfCE89E,
0x43EEbfd2F479CcE1108fCa5E2438166FA42d3f14,
0x6E777F42Ac66f18c1951cA915891009c93FEA266,
0xf6Cf3559D018A5A3831f84893aef9031a686F991,
0x34cfbf5820C00636D4d620D339e202aBAB44972D,
0xB8832b130B3B3da1b9B3B7E8C762eEE9CCF47BbA,
0x85F3Eef327c307e956a5f152846F5bF1c05E1883,
0x7a7238181EACB322ae27430A15B1aF38d56F05bF,
0x22f52Afe4c458A1267Be49aC9541CE7DFFC08a70,
0xFEDd89CcC37346c914EC779614c2201E7df21F81,
0x02CceD73071754a2AAeaB512A60705bb8d3314A8,
0x29E1a77d13aE74d16CD9cD8768C8f5989e3fb7d1,
0x9dD957a1268b18b7a941A0c8e03EB390d7a74Ad1,
0xbe23120FCe3da336f0E581df9C4D9708FD331D3D,
0x69956209b2b1308a1ABA80bFB54248Dd57154DA8,
0xe82E5bbF3787975b822CC5495e45b708F71f0a8B,
0xE0Fe1A9648b683cf1b3e69A6eC14D09b9e3F091f,
0xD4C8beA00CC971CBC54b2a51710436219fc4Dda8,
0x8eE221dFdFae37655c688C9A309BdB3C0d6aaa74,
0xdC3dAF3ab9f04Fb631D6F8329767Fe1c2BD0f6EC,
0x3CFAc6f285BEEeC589981Fa3087296f5520C369D,
0xdA7c8338bfD86507388e13EFC1051de3EA15f313,
0x5ad61630a437a7B243Ee84829CEc1C4EeDF7Abe0,
0x7f5d1E0699eac9F7cC908cfCF681e5f5A8427E0C,
0x1eA2DD6A937A50f87d4df00ee16dF3296fF1E2cd,
0xac9f7356728E4c412993CA688Cf3c5E29bd73317,
0x3aa76B806d1FC58019759F3529d764F98dC8C410,
0x27D694a0589454b4E649B693cb4c5260df80f376,
0x09B059bD114B2F1Be1BbdcC53c7B0D2129f7eB7D,
0x410C648eF1db2Ab0fc268011af11dc9A129a4847,
0xB4938add58Ebb8a3118F6A61AB76De0B47ba45E3,
0x62E9Bb1Fc6a161ebcA96E3f8788E4c04b1e324aE,
0x30fF14908142307e41Aa482b25BBE7fdEE4468E1,
0x665EE0a67A2F7C2320C610f038C17fa647e6c71D,
0x672DF65288534fead5aC4d40A29637b8a9c99ad5,
0x9d39815897FBE436697738F8d938b22eF67FB7B0,
0x7FE1D01AFeC94C456BBED191578326f0b6e24d85,
0x0D396528B853bF145D94446695d8FFFA7135bFAd,
0xCc8F9A4890f997C45CAfF020A0c2239e919Eb7f5,
0x291B1944fC4d1658c7Aa619fFeD3F07E5925B40B,
0xc838526Bd0B4ce3006E808E7ab8f4002e2bC7E92,
0xc177933100bD5A683e94F8F286C89bB668Bce6e6,
0x3dCd72B35AD6Ae594bAFC1629368B25A9a8aE970,
0x0372AEED41d5d6295FE335b4B3c58E73C7E1874F,
0x8131b72E943123badf23D52864638432E175D05A,
0x58B83A0fCbf976a6a2143875a71F3100ADeA0AC4,
0x15ed066b939403A8591F860a0035eAd1b1faF3BE,
0xb52bF827233896A6D9A66F428Db860B20623708E,
0x00e9b14B3f11835A43728Cd8BfD9D21A1978eEb8,
0x4759D6D0dD7d2c55390B1968c6a1C0F1c433f20e,
0x09C23aE5798247DFA312Be3538c8B1BD71E7E591,
0xCc3399b1E00b5Eb3ee74Ef0f639192F36A9f0002,
0x6Cb7eDaFB75715C463D5cFfE299174c46b58Dc06,
0xCFc29D954b1a92aE2c659C4BF719628cDB604e08,
0x2a48DB21c691cf26fF12Df84476125F51824b909,
0x1529bf3fb64E90585227544303faF030f31d09C0,
0xe7e9033363B988d46fEa4cA7d80ecFc1215eD436,
0x1801EDe5aB6ba4429Ea2aE78feF1AaDc3bc11372,
0x61A43dF882A9Fbd51B8674802DC29B83B946e272,
0xF3f591E0622a6Fbf19D1922d6e31f7dcdb55d213,
0x7eEFC2B145edA7F9DdC6cbE96489e927e3f11489,
0xDBA15D7DdE4144d111BAbE028743B71D5C4baA30,
0x9F0536E72cC48e395a77C40cb041ad3d27AE4623,
0xbeE0cE3FEB29a2832B1203a24e1723aEDC3CbCa1,
0x714DAC652F8534e639514144402bfDd585A776A7,
0x362623Be3C417DC583D4b6E81989d2FF29Ea8a40,
0x713B4d8deCcEa1219E8ad8D4F3dF8575E3F2861D,
0x6DcC347080CBD8E8F0B1a59a8b9Fa6cd9B987d01,
0xa6b6EA5114A589Ac025B80b8773A6F1f3F4A9786,
0xCEf94a714A0a544A2f928818c34743a11Cedc51a,
0x21b9490B88E9CF002Dc83bD4e1A1d47109469757,
0x6bCF134D928270A0d865e95980a652340A79a841,
0xCe40743e776B7F711b2d817Cc0f7321CEE4f31a9,
0x4E4a885a977AEA351D8bE069d41c548C08c2C6c6,
0x073cf98321FDEB73c399Af73F9076fd9ACC5a869,
0x1c873Ac2433FB54d2a708E639Dbb6AddAf4ac319,
0xD1d38a8b250f33C2d91C2a2403EDAa1Cb2bffBB5,
0xD0B9bfaC299b2F5FCcA19b011e65F2A76e12447C,
0x28F31930b935bD0557cECe5AfC98641014930DFa,
0xCb61Ec812D7C2Fc1143637079591614C022c696A,
0x448A77F0Ecbd2bD96D3DdA5352AC5Ac20bB453Ba,
0x5433001eA8Ea88F98d62AE5F3AF7D35E055FB992,
0x4756Beb08C30e269f22E4b368a37A38ea6Ba9d22,
0xB42DbADD61DBDeAB44537E57ADe6A4a2811a64C3,
0x17ac05Cdd4d000DA78b87491C6ED8C87C81146BB];
        for(uint i = 0; i < users.length; i++){
            perm[users[i]] = true;
        }
        mask = 1;
        logmask = 0;
    }

    function problem1() external payable {
        assert(!p1[msg.sender]);
        assert(perm[msg.sender]);
        msg.sender.transfer(10 ether);
        p1[msg.sender] = true;
    }

    function problem2(uint nonce) external payable {
        assert(!p2[msg.sender]);
        assert(perm[msg.sender]);
        uint256 hash = uint256(keccak256(abi.encode(nonce,msg.sender)));
        uint256 temp = hash % mask;
        if(temp == 0) {
            msg.sender.transfer(30 ether);
            p2[msg.sender] = true;
            if(logmask < 34) {
                mask = mask<<1;
                logmask += 1;
            }
        }

    }
    
    mapping (address => uint) private last_block;
    function problem3() external payable {
        assert(!p3[msg.sender]);
        assert(perm[msg.sender]);
        assert(block.number != last_block[msg.sender]);
        uint dice = uint(keccak256(abi.encode(msg.sender,block.number,now))) %6;
        last_block[msg.sender] = block.number;
        if(dice == 0){
            msg.sender.transfer(10 ether);
            p3[msg.sender] = true;
        }
    }


    function problem4() external payable {
        assert(!p4[msg.sender]);
        assert(perm[msg.sender]);
        assert(msg.value == 3.14159265 ether);
        msg.sender.transfer(23.14159265 ether);
        p4[msg.sender] = true;
    }
    
    
    function problem5(uint nonce) external payable {
        assert(!p5[msg.sender]);
        assert(perm[msg.sender]);
        uint256 hash = uint256(keccak256(abi.encode(nonce)));
        uint256 expected = 0x211564A164F2D11471141079C465DB7481ECE38B4226000C1F9949F6F3C81B10;
        if(hash == expected){
            msg.sender.transfer(30 ether);
            p5[msg.sender] = true;
        }
    }
}
