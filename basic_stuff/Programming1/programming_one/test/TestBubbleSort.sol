pragma solidity >=0.5.0 <=0.8.18; // Do NOT change this line

import "truffle/Assert.sol";
import "truffle/DeployedAddresses.sol";
import "../contracts/Sorter.sol";



// Test Implementations of Bubble Sort
contract TestBubbleSort {
    // Arrays to Sort
    uint[] array1 = [1,3,6]; // Already sorted
    uint[] array2 = [1, 0]; // 1 Element
    uint[] array3 = [3,2]; // 1 Element
    uint[] array4 = [1,6,3,6,6,3,3,4,0]; // 1 Element
    uint[] array5 = []; // 1 Element

    // Sorted arrays
    uint[] expected1 = [1,3,6];
    uint[] expected2 = [0, 1];
    uint[] expected3 = [2,3];
    uint[] expected4 = [0,1,3,3,3,4,6,6,6];
    uint[] expected5 = [];

    // Tests

    function iterativeArraySort(uint[] memory _array, uint[] memory _expected) internal {
        Sorter sorter = Sorter(DeployedAddresses.Sorter());
	Assert.equal(sorter.iterativeBubbleSort(_array), _expected, "Array is not sorted");
    }

    function recursiveArraySort(uint[] memory _array, uint[] memory _expected) internal {
        Sorter sorter = Sorter(DeployedAddresses.Sorter());
	Assert.equal(sorter.recursiveBubbleSort(_array, uint8(_array.length)), _expected, "Array is not sorted");
    }

    // Test Case 1
    function testIterativeArraySortOne() public {
        iterativeArraySort(array1, expected1);
    }

    // Test Case 2
    function testIterativeArraySortTwo() public {
        iterativeArraySort(array2, expected2);
    }

    // Test Case 3 
    function testRecursiveArraySortOne() public {
        recursiveArraySort(array1, expected1);
    }

    // Test Case 4
    function testRecursiveArraySortTwo() public {
        recursiveArraySort(array2, expected2);
    }



    function testIterativeArraySortThree() public {
        iterativeArraySort(array3, expected3);
    }

    function testRecursiveArraySortThree() public {
        recursiveArraySort(array3, expected3);
    }

    function testIterativeArraySortFour() public {
        iterativeArraySort(array4, expected4);
    }

    function testRecursiveArraySortFour() public {
        recursiveArraySort(array4, expected4);
    }
    
    function testIterativeArraySortFive() public {
        iterativeArraySort(array5, expected5);
    }

    function testRecursiveArraySortFive() public {
        recursiveArraySort(array5, expected5);
    }

}
