
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { CHART_COLORS } from '../assets/utils';
import './BarChart.css'
import Popup from './Popup';
import React, { useEffect, useState } from 'react';

// Register the required components
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const BarGraph = ({dataa}) => {

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [modalContent, setModalContent] = useState('');
  const data = {
    labels: dataa['labels'], // Department names
    datasets: [
      {
        label: 'Data',
        data: dataa['data'], // Corresponding average salaries
        backgroundColor: Object.values(CHART_COLORS),
        borderWidth: 0,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      tooltip: {
        callbacks: {
          label: function (tooltipItem) {
            let percentage = (
              (tooltipItem.raw /
                tooltipItem.chart._metasets[0].total) *
              100
            ).toFixed(2);
            return `${tooltipItem.label}: ${tooltipItem.raw}`;
          },
        },
      },
    },
    onClick: (event, elements) => {
      if (elements.length > 0) {
        const index = elements[0].index;
        setModalContent(`You clicked on ${data.labels[index]}`);
        setIsModalOpen(true);
      }
    },
  };

  return (
    <div className='bar-chart-container mt-10'>
      <h2>Company Salary Data</h2>
      <Bar data={data} options={options}/>
      <Popup
      show={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        content={modalContent}
      />
    </div>
  );
};

export default BarGraph;
