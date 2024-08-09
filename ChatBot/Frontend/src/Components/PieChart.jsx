// src/components/PieChart.js
import { Doughnut, Pie } from 'react-chartjs-2';
import { Chart, ArcElement, Tooltip, Legend } from 'chart.js';
import './PieChart.css'
import { CHART_COLORS } from '../assets/utils';
import Popup from './Popup';
import React, { useEffect, useState } from 'react';

Chart.register(ArcElement, Tooltip, Legend);


const PieChart = ({dataa}) => {

   const [isModalOpen, setIsModalOpen] = useState(false);
  const [modalContent, setModalContent] = useState('');
  const data = {
    labels: dataa['labels'],
    datasets: [
      {
        label:"",
        data: dataa['data'],
        backgroundColor: Object.values(CHART_COLORS),
        borderWidth: 2,
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
            return `${tooltipItem.label}: ${tooltipItem.raw} (${percentage}%)`;
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
    <div className='pie-chart-container'>
      <h2>Interactive Pie Chart</h2>
      <Doughnut data={data} options={options} height={30} width={30}/>
      <Popup
      show={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        content={modalContent}
      />
    </div>
  );
};

export default PieChart;
