pragma solidity ^0.8.18;

// SPDX-License-Identifier: MIT

contract A {
    function foo(uint x) public pure returns (uint) {
        return (x != 10 ? x > 10 : x < 10) ? 1 : 2;
    }
}

