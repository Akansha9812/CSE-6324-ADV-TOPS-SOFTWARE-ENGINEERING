// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract LoopContract {
    uint256 public variableA;
    uint256 public variableB;
    uint256 public variableC;
    
    function computeValue() public {
        variableA = variableB + 1;
        variableB = variableC + 2;
        variableC = variableC * 2;
    }
    
    function infiniteLoop() public {
        while (true) {
            computeValue();
        }
    }
}
