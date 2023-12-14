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

    function donate() external payable {}
    uint public mask;
    uint public logmask;
    constructor() public{
        owner = msg.sender;
        users = [0x2a48DB21c691cf26fF12Df84476125F51824b909];
        for(uint i = 0; i < users.length; i++){
            perm[users[i]] = true;
        }
        mask = 1;
        logmask = 0;
    }

    function problem1() external payable {
        assert(!p1[msg.sender]);
        assert(perm[msg.sender]);
        console.log("console output %s", msg.sender);
        p1[msg.sender] = true;
    }

    function problem2(uint nonce) external payable {
        assert(!p2[msg.sender]);
        assert(perm[msg.sender]);
        uint256 hash = uint256(keccak256(abi.encode(nonce,msg.sender)));
        uint256 temp = hash % mask;
        console.log("console output %d", temp);
        if(temp == 0) {

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

            p3[msg.sender] = true;
        }
    }


    function problem4() external payable {
        assert(!p4[msg.sender]);
        assert(perm[msg.sender]);
        assert(msg.value == 3.14159265 ether);

        p4[msg.sender] = true;
    }
    
    
    function problem5(uint nonce) external payable {
        assert(!p5[msg.sender]);
        assert(perm[msg.sender]);
        uint256 hash = uint256(keccak256(abi.encode(nonce)));
        uint256 expected = 0x211564A164F2D11471141079C465DB7481ECE38B4226000C1F9949F6F3C81B10;
        if(hash == expected){

            p5[msg.sender] = true;
        }
    }
}
