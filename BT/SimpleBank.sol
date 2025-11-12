// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/// @title SimpleBank - a single-customer bank account contract
/// @author
/// @notice Deposit, withdraw and check balance for the account owner
contract SimpleBank {
    address payable public owner;
    uint256 public lastDepositTimestamp;

    // Reentrancy guard (simple)
    uint256 private locked = 1;

    // Events
    event Deposited(address indexed from, uint256 amount);
    event Withdrawn(address indexed to, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "SimpleBank: caller is not the owner");
        _;
    }

    modifier nonReentrant() {
        require(locked == 1, "SimpleBank: reentrant call");
        locked = 2;
        _;
        locked = 1;
    }

    constructor() {
        owner = payable(msg.sender);
        emit OwnershipTransferred(address(0), owner);
    }

    /// @notice Accept direct ETH transfers as deposits
    receive() external payable {
        _deposit();
    }

    /// @notice Fallback to accept deposits (if calldata present)
    fallback() external payable {
        _deposit();
    }

    /// @notice Deposit ether into the contract
    /// @dev Emits Deposited event
    function deposit() external payable {
        _deposit();
    }

    /// @dev Internal deposit implementation
    function _deposit() internal {
        require(msg.value > 0, "SimpleBank: deposit value must be > 0");
        lastDepositTimestamp = block.timestamp;
        emit Deposited(msg.sender, msg.value);
    }

    /// @notice Withdraw `amount` wei to the owner address
    /// @param amount Amount in wei to withdraw
    /// @dev Only owner can call. Uses nonReentrant guard and checks-effects-interactions pattern.
    function withdraw(uint256 amount) external onlyOwner nonReentrant {
        require(amount > 0, "SimpleBank: withdraw amount must be > 0");
        uint256 bal = address(this).balance;
        require(amount <= bal, "SimpleBank: insufficient balance");

        // Effects done; now interactions
        // use call to forward all gas and check success
        (bool success, ) = owner.call{value: amount}("");
        require(success, "SimpleBank: transfer failed");

        emit Withdrawn(owner, amount);
    }

    /// @notice Withdraw entire contract balance to owner
    function withdrawAll() external onlyOwner nonReentrant {
        uint256 bal = address(this).balance;
        require(bal > 0, "SimpleBank: no balance to withdraw");

        (bool success, ) = owner.call{value: bal}("");
        require(success, "SimpleBank: transfer failed");
        emit Withdrawn(owner, bal);
    }

    /// @notice Returns current contract (account) balance in wei
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /// @notice Allows owner to transfer ownership to a new owner
    /// @param newOwner Address of the new owner
    function transferOwnership(address payable newOwner) external onlyOwner {
        require(newOwner != address(0), "SimpleBank: new owner is zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}