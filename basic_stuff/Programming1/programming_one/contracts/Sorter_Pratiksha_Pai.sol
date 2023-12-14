pragma solidity >=0.5.0 <=0.8.18;

/*
 * TESTS
 * We will test your code with our test cases by calling 'truffle test'
 * We are using truffle's automated testing framework
 * We wrote the tests in Solidity but it is also possible to use JavaScript's Mocha framework
 * Learn how to test: https://www.trufflesuite.com/docs/truffle/testing/writing-tests-in-solidity
 * 10 test cases, each is worth 8 points (5 test cases for iterative bubble sort, 5 for recursive)
 * You are encouraged to write your own test cases
 *
 * ORDER
 * Sort from SMALLEST TO LARGEST uint
 *
 * EXAMPLES
 * Input: uint[] array = [4,3,2,3];
 * Output: uint[] expected = [2,3,3,4];
 *
 * NOTE
 * We WILL VERIFY you wrote an iterative/recursive bubble sort as instructed
 * Writing two iterative or two recursive solutions will result in 0 points for the whole assignment
 */

// Implement Bubble sorts (Do NOT rename the contract)
contract Sorter {
    function _swap(uint a, uint b) internal pure returns (uint x, uint y){
        return (b,a);
    }

    function iterativeBubbleSort(uint[] memory _data) public pure returns (uint[] memory) {
        uint n = _data.length;
        for (uint i=0; i<n-1; i++){
            for (uint j=0; j<n-1-i; j++){
                if (_data[j] > _data[j+1]){
                    (_data[j], _data[j+1]) = _swap(_data[j], _data[j+1]);
                }
            }
        }
        
        return _data;
    }

    function recursiveBubbleSort(uint[] memory _data, uint8 _size) public pure returns (uint[] memory) {

        if (_size == 1){
            return _data;
        }
        uint count = 0;
        for (uint j=0; j<_size-1; j++){
            if (_data[j] > _data[j+1]){
                (_data[j], _data[j+1]) = _swap(_data[j], _data[j+1]);
                count++;
            }
        }

        if(count == 0){
            return _data;
        }
        recursiveBubbleSort(_data, _size-1);

        return _data;
    }
}
