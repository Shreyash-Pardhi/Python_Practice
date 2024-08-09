import React, { useEffect, useState } from 'react';
import PieChart from './Components/PieChart';
import BarGraph from './Components/BarChart';

const processDepartmentData = (employees) => {
  const departmentCounts = employees.reduce((acc, emp) => {
    acc[emp.work_dept] = (acc[emp.work_dept] || 0) + 1;
    return acc;
  }, {});

  const labels = Object.keys(departmentCounts);
  const data = Object.values(departmentCounts);

  return { labels, data };
};

const processAverageSalaryData = (employees) => {
  // Calculate the total salary and count of employees for each department
  const departmentSalaryData = employees.reduce((acc, emp) => {
    if (!acc[emp.work_dept]) {
      acc[emp.work_dept] = { totalSalary: 0, count: 0 };
    }
    acc[emp.work_dept].totalSalary += emp.salary;
    acc[emp.work_dept].count += 1;
    return acc;
  }, {});

  // Calculate the average salary for each department
  const labels = Object.keys(departmentSalaryData);
  const data = labels.map(dept => departmentSalaryData[dept].totalSalary / departmentSalaryData[dept].count);

  return { labels, data };
};

const processAverageSalaryByGender = (employees) => {
  // Calculate the total salary and count of employees for each gender
  const genderSalaryData = employees.reduce((acc, emp) => {
    if (!acc[emp.gender]) {
      acc[emp.gender] = { totalSalary: 0, count: 0 };
    }
    acc[emp.gender].totalSalary += emp.salary;
    acc[emp.gender].count += 1;
    return acc;
  }, {});

  // Calculate the average salary for each gender
  const labels = Object.keys(genderSalaryData);
  const data = labels.map(gender => genderSalaryData[gender].totalSalary / genderSalaryData[gender].count);

  return { labels, data };
};

const processGenderCount = (employees) => {
  // Calculate the count of employees for each gender
  const genderCountData = employees.reduce((acc, emp) => {
    acc[emp.gender] = (acc[emp.gender] || 0) + 1;
    return acc;
  }, {});

  // Get the labels (genders) and data (counts)
  const labels = Object.keys(genderCountData);
  const data = Object.values(genderCountData);

  return { labels, data };
};

function App () {

  const [emp_data, setEmp_data] = useState([])

  useEffect(() => {
    fetch('http://127.0.0.1:5000/employees')
      .then(response => response.json())
      .then(data => setEmp_data(data))
  }, [])


  const departmentData = processDepartmentData(emp_data);
  const AvgSalData = processAverageSalaryData(emp_data);
  const AvgSalGender = processAverageSalaryByGender(emp_data);
  const GenCount = processGenderCount(emp_data);

  return (
    <div className='flex flex-wrap'>
      <div>
        <pre>{JSON.stringify(departmentData)}</pre>
        <PieChart
        dataa={departmentData}
        />
      </div>
      <div>
        <pre className='mt-10'>{JSON.stringify(AvgSalData)}</pre>
        <BarGraph
        dataa={AvgSalData}
        />
      </div>
      <div>
        <pre className='mt-10'>{JSON.stringify(AvgSalGender)}</pre>
        <BarGraph
        dataa={AvgSalGender}
        />
      </div>
      <div>
        <pre className='mt-10'>{JSON.stringify(GenCount)}</pre>
        <PieChart
        dataa={GenCount}
        />
      </div>
    </div>
  );
};

export default App;
