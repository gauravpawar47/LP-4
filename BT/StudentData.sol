// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    // Structure to represent a student
    struct Student {
        uint256 rollNo;
        string name;
        uint256 marks;
    }

    // Dynamic array to store multiple students
    Student[] public students;

    // Event for logging student addition
    event StudentAdded(uint256 rollNo, string name, uint256 marks);

    // Function to add a student
    function addStudent(uint256 _rollNo, string memory _name, uint256 _marks) public {
        students.push(Student(_rollNo, _name, _marks));
        emit StudentAdded(_rollNo, _name, _marks);
    }

    // Function to get student details by index
    function getStudent(uint256 index) public view returns (uint256, string memory, uint256) {
        require(index < students.length, "Invalid index");
        Student memory s = students[index];
        return (s.rollNo, s.name, s.marks);
    }

    // Function to get total number of students
    function getTotalStudents() public view returns (uint256) {
        return students.length;
    }

    // Fallback function — gets called if non-existent function or Ether is sent
    fallback() external payable {
        // Any Ether sent here will be accepted but not used
    }

    // Receive Ether directly (optional)
    receive() external payable {}
}
