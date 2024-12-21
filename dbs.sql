CREATE TABLE Departments (
    DepartmentID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Location VARCHAR(100) NOT NULL
);

CREATE TABLE Doctors (
    DoctorID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Specialization VARCHAR(50) NOT NULL,
    Phone VARCHAR(15) NOT NULL,
    DepartmentID INT NOT NULL,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Age INT NOT NULL,
    Gender VARCHAR(10) NOT NULL,
    Phone VARCHAR(15) NOT NULL
);

CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,
    Date DATE NOT NULL,
    Time TIME NOT NULL,
    Status VARCHAR(20) NOT NULL,
    PatientID INT NOT NULL,
    DoctorID INT NOT NULL,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
);







INSERT INTO Departments (Name, Location) VALUES ('Cardiology', 'Building A');
INSERT INTO Departments (Name, Location) VALUES ('Neurology', 'Building B');
INSERT INTO Departments (Name, Location) VALUES ('Orthopedics', 'Building C');
INSERT INTO Departments (Name, Location) VALUES ('Pediatrics', 'Building D');
INSERT INTO Departments (Name, Location) VALUES ('Oncology', 'Building E');


INSERT INTO Doctors (Name, Specialization, Phone, DepartmentID) VALUES ('Dr. John Smith', 'Cardiologist', '1234567890', 1);
INSERT INTO Doctors (Name, Specialization, Phone, DepartmentID) VALUES ('Dr. Jane Doe', 'Neurologist', '1234567891', 2);
INSERT INTO Doctors (Name, Specialization, Phone, DepartmentID) VALUES ('Dr. Alan Grant', 'Orthopedist', '1234567892', 3);
INSERT INTO Doctors (Name, Specialization, Phone, DepartmentID) VALUES ('Dr. Emily Rose', 'Pediatrician', '1234567893', 4);
INSERT INTO Doctors (Name, Specialization, Phone, DepartmentID) VALUES ('Dr. Mark Green', 'Oncologist', '1234567894', 5);


INSERT INTO Patients (Name, Age, Gender, Phone) VALUES ('Alice Johnson', 34, 'Female', '9876543210');
INSERT INTO Patients (Name, Age, Gender, Phone) VALUES ('Bob Brown', 45, 'Male', '9876543211');
INSERT INTO Patients (Name, Age, Gender, Phone) VALUES ('Charlie Black', 29, 'Male', '9876543212');
INSERT INTO Patients (Name, Age, Gender, Phone) VALUES ('Diana White', 40, 'Female', '9876543213');
INSERT INTO Patients (Name, Age, Gender, Phone) VALUES ('Eve Adams', 25, 'Female', '9876543214');


INSERT INTO Appointments (Date, Time, Status, PatientID, DoctorID) VALUES ('2024-12-21', '10:00:00', 'Confirmed', 1, 1);
INSERT INTO Appointments (Date, Time, Status, PatientID, DoctorID) VALUES ('2024-12-22', '11:00:00', 'Pending', 2, 2);
INSERT INTO Appointments (Date, Time, Status, PatientID, DoctorID) VALUES ('2024-12-23', '12:00:00', 'Cancelled', 3, 3);
INSERT INTO Appointments (Date, Time, Status, PatientID, DoctorID) VALUES ('2024-12-24', '09:30:00', 'Confirmed', 4, 4);
INSERT INTO Appointments (Date, Time, Status, PatientID, DoctorID) VALUES ('2024-12-25', '14:00:00', 'Pending', 5, 5);
