// MIDOR GHG Inventory - Chart Functions
// Using ECharts with SVG renderer for print quality

// Color scheme (from PRD)
const COLORS = {
  scope1: '#F59E0B', // Amber
  scope2: '#3B82F6', // Blue
  scope3: '#1E40AF', // Navy
  teal: '#14B8A6',
  blue: '#06B6D4',
  warmAccent: '#F97316',
  gray: '#6B7280',
  lightGray: '#E5E7EB'
};

// Utility: Format numbers with commas
function formatNumber(num) {
  return num.toLocaleString('en-US', { maximumFractionDigits: 0 });
}

// Utility: Format to millions
function formatMillion(num) {
  return (num / 1_000_000).toFixed(2) + ' Mt';
}

// 1. Chevron/Ribbon Share Chart (for Scope overview)
function makeChevronShare(elementId, data) {
  const chart = echarts.init(document.getElementById(elementId), null, { renderer: 'svg' });

  const total = data.scope1 + data.scope2 + data.scope3;
  const percentages = {
    scope1: ((data.scope1 / total) * 100).toFixed(1),
    scope2: ((data.scope2 / total) * 100).toFixed(1),
    scope3: ((data.scope3 / total) * 100).toFixed(1)
  };

  const option = {
    backgroundColor: 'transparent',
    title: {
      text: 'GHG Inventory by Scope',
      left: 'center',
      textStyle: { fontSize: 18, fontWeight: 600 }
    },
    tooltip: {
      trigger: 'item',
      formatter: '{b}: {c} tCO₂e ({d}%)'
    },
    series: [{
      type: 'pie',
      radius: ['40%', '70%'],
      avoidLabelOverlap: false,
      label: {
        show: true,
        fontSize: 14,
        fontWeight: 600,
        formatter: '{b}\n{d}%\n{c} tCO₂e'
      },
      labelLine: { show: true },
      data: [
        { value: data.scope1, name: 'Scope 1', itemStyle: { color: COLORS.scope1 } },
        { value: data.scope2, name: 'Scope 2', itemStyle: { color: COLORS.scope2 } },
        { value: data.scope3, name: 'Scope 3', itemStyle: { color: COLORS.scope3 } }
      ]
    }]
  };

  chart.setOption(option);
  window.addEventListener('resize', () => chart.resize());
  return chart;
}

// 2. Stacked Bar Chart by Category
function makeStackedByCategory(elementId, categories, title) {
  const chart = echarts.init(document.getElementById(elementId), null, { renderer: 'svg' });

  const categoryNames = Object.keys(categories);
  const values = categoryNames.map(cat => categories[cat].total);

  const option = {
    backgroundColor: 'transparent',
    title: {
      text: title,
      left: 'center',
      textStyle: { fontSize: 16, fontWeight: 600 }
    },
    tooltip: {
      trigger: 'axis',
      axisPointer: { type: 'shadow' },
      formatter: '{b}: {c} tCO₂e'
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: {
      type: 'value',
      axisLabel: {
        formatter: (value) => (value / 1000).toFixed(0) + 'k'
      }
    },
    yAxis: {
      type: 'category',
      data: categoryNames,
      axisLabel: {
        fontSize: 11,
        interval: 0
      }
    },
    series: [{
      type: 'bar',
      data: values,
      itemStyle: {
        color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
          { offset: 0, color: COLORS.teal },
          { offset: 1, color: COLORS.blue }
        ])
      },
      label: {
        show: true,
        position: 'right',
        formatter: (params) => formatNumber(params.value),
        fontSize: 10
      }
    }]
  };

  chart.setOption(option);
  window.addEventListener('resize', () => chart.resize());
  return chart;
}

// 3. Supplier Split (for Scope 2)
function makeSupplierSplit(elementId, suppliers) {
  const chart = echarts.init(document.getElementById(elementId), null, { renderer: 'svg' });

  const data = Object.keys(suppliers).map(name => ({
    name: name,
    value: suppliers[name].emissions_tCO2e
  }));

  const option = {
    backgroundColor: 'transparent',
    title: {
      text: 'Scope 2: Electricity by Supplier',
      left: 'center',
      textStyle: { fontSize: 16, fontWeight: 600 }
    },
    tooltip: {
      trigger: 'item',
      formatter: '{b}: {c} tCO₂e ({d}%)'
    },
    series: [{
      type: 'pie',
      radius: '60%',
      data: data,
      label: {
        fontSize: 12,
        formatter: '{b}\n{d}%'
      },
      itemStyle: {
        color: (params) => {
          const colors = [COLORS.scope2, COLORS.blue];
          return colors[params.dataIndex];
        }
      }
    }]
  };

  chart.setOption(option);
  window.addEventListener('resize', () => chart.resize());
  return chart;
}

// 4. Heat Tiles (for facility/unit emissions)
function makeHeatTiles(elementId, activities, categoryName) {
  const chart = echarts.init(document.getElementById(elementId), null, { renderer: 'svg' });

  // Sort by emissions
  const sorted = activities.sort((a, b) => b.emissions_tCO2e - a.emissions_tCO2e).slice(0, 20);

  const names = sorted.map(a => a.sub_activity || a.activity);
  const values = sorted.map(a => a.emissions_tCO2e);

  const option = {
    backgroundColor: 'transparent',
    title: {
      text: `Top Emission Sources: ${categoryName}`,
      left: 'center',
      textStyle: { fontSize: 14, fontWeight: 600 }
    },
    tooltip: {
      trigger: 'axis',
      axisPointer: { type: 'shadow' },
      formatter: '{b}: {c} tCO₂e'
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: {
      type: 'value',
      axisLabel: {
        formatter: (value) => (value / 1000).toFixed(0) + 'k'
      }
    },
    yAxis: {
      type: 'category',
      data: names,
      axisLabel: {
        fontSize: 9,
        interval: 0
      }
    },
    series: [{
      type: 'bar',
      data: values,
      itemStyle: {
        color: COLORS.warmAccent
      },
      label: {
        show: true,
        position: 'right',
        formatter: (params) => formatNumber(params.value),
        fontSize: 9
      }
    }]
  };

  chart.setOption(option);
  window.addEventListener('resize', () => chart.resize());
  return chart;
}

// 5. Waterfall Chart (for Scope 3 products)
function makeWaterfall(elementId, products) {
  const chart = echarts.init(document.getElementById(elementId), null, { renderer: 'svg' });

  const names = products.map(p => p.product);
  const values = products.map(p => p.emissions_tCO2e);

  const option = {
    backgroundColor: 'transparent',
    title: {
      text: 'Scope 3 Category 11: Use of Sold Products',
      left: 'center',
      textStyle: { fontSize: 16, fontWeight: 600 }
    },
    tooltip: {
      trigger: 'axis',
      axisPointer: { type: 'shadow' },
      formatter: '{b}: {c} tCO₂e'
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '15%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: names,
      axisLabel: {
        rotate: 45,
        fontSize: 10
      }
    },
    yAxis: {
      type: 'value',
      axisLabel: {
        formatter: (value) => (value / 1_000_000).toFixed(1) + 'M'
      }
    },
    series: [{
      type: 'bar',
      data: values,
      itemStyle: {
        color: COLORS.scope3
      },
      label: {
        show: true,
        position: 'top',
        formatter: (params) => (params.value / 1_000_000).toFixed(2) + 'M',
        fontSize: 9
      }
    }]
  };

  chart.setOption(option);
  window.addEventListener('resize', () => chart.resize());
  return chart;
}

// 6. Sparkline KPI (for intensities)
function makeSparkKPI(elementId, value, unit, label, trendData = null) {
  const chart = echarts.init(document.getElementById(elementId), null, { renderer: 'svg' });

  // If no trend data, show just the value
  if (!trendData) {
    trendData = [value * 0.95, value * 0.98, value];
  }

  const option = {
    backgroundColor: 'transparent',
    title: {
      text: label,
      left: 'center',
      top: 10,
      textStyle: { fontSize: 12, fontWeight: 500, color: COLORS.gray }
    },
    graphic: [{
      type: 'text',
      left: 'center',
      top: 'center',
      style: {
        text: value.toString(),
        fontSize: 32,
        fontWeight: 700,
        fill: COLORS.scope1
      }
    }, {
      type: 'text',
      left: 'center',
      top: '60%',
      style: {
        text: unit,
        fontSize: 12,
        fill: COLORS.gray
      }
    }],
    xAxis: {
      type: 'category',
      show: false,
      data: ['2023', '2024', '2025']
    },
    yAxis: {
      type: 'value',
      show: false
    },
    grid: {
      left: 0,
      right: 0,
      top: '80%',
      bottom: 0
    },
    series: [{
      type: 'line',
      data: trendData,
      smooth: true,
      showSymbol: false,
      lineStyle: {
        color: COLORS.teal,
        width: 2
      },
      areaStyle: {
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          { offset: 0, color: 'rgba(20, 184, 166, 0.3)' },
          { offset: 1, color: 'rgba(20, 184, 166, 0.05)' }
        ])
      }
    }]
  };

  chart.setOption(option);
  window.addEventListener('resize', () => chart.resize());
  return chart;
}

// 7. Scope 1 Gas Split (CO2, CH4, N2O)
function makeGasSplit(elementId) {
  const chart = echarts.init(document.getElementById(elementId), null, { renderer: 'svg' });

  // Typical refinery gas split (CO2 dominant, CH4 and N2O small)
  const gasData = [
    { name: 'CO₂', value: 96.5, color: '#94A3B8' },
    { name: 'CH₄ (as CO₂e)', value: 2.8, color: '#F59E0B' },
    { name: 'N₂O (as CO₂e)', value: 0.7, color: '#EF4444' }
  ];

  const option = {
    backgroundColor: 'transparent',
    title: {
      text: 'Scope 1: GHG Composition',
      left: 'center',
      textStyle: { fontSize: 14, fontWeight: 600 }
    },
    tooltip: {
      trigger: 'item',
      formatter: '{b}: {c}%'
    },
    series: [{
      type: 'pie',
      radius: '60%',
      data: gasData.map(g => ({
        name: g.name,
        value: g.value,
        itemStyle: { color: g.color }
      })),
      label: {
        fontSize: 11,
        formatter: '{b}\n{c}%'
      }
    }]
  };

  chart.setOption(option);
  window.addEventListener('resize', () => chart.resize());
  return chart;
}

// 8. Timeline/Roadmap for mitigation initiatives
function makeRoadmapTimeline(elementId) {
  const container = document.getElementById(elementId);

  const initiatives = [
    { year: 2025, title: 'Energy Management System (ISO 50001)', reduction: 'Monitoring baseline' },
    { year: 2026, title: 'Solar PV Installation (5 MW)', reduction: '~8,000 tCO₂e/yr' },
    { year: 2027, title: 'Waste Heat Recovery', reduction: '~12,000 tCO₂e/yr' },
    { year: 2028, title: 'Fleet Electrification', reduction: '~3,000 tCO₂e/yr' },
    { year: 2029, title: 'LDAR Enhancement Program', reduction: '~5,000 tCO₂e/yr' },
    { year: 2030, title: 'Real-time Emissions Monitoring', reduction: 'Optimization' }
  ];

  let html = '<div class="roadmap-timeline">';
  initiatives.forEach((item, idx) => {
    html += `
      <div class="timeline-item" style="animation-delay: ${idx * 0.1}s">
        <div class="timeline-year">${item.year}</div>
        <div class="timeline-content">
          <div class="timeline-title">${item.title}</div>
          <div class="timeline-reduction">${item.reduction}</div>
        </div>
      </div>
    `;
  });
  html += '</div>';

  container.innerHTML = html;
}

// Utility: Initialize all charts after page load
function initializeAllCharts() {
  // Check if MIDOR_DATA is loaded
  if (typeof MIDOR_DATA === 'undefined') {
    console.error('MIDOR_DATA not loaded!');
    return;
  }

  // Chevron Share (Section 5)
  if (document.getElementById('chart-chevron-share')) {
    makeChevronShare('chart-chevron-share', MIDOR_DATA.totals);
  }

  // Scope 1 by Category (Section 6)
  if (document.getElementById('chart-scope1-category')) {
    makeStackedByCategory('chart-scope1-category', MIDOR_DATA.scope1.categories, 'Scope 1 by Category');
  }

  // Scope 1 Heat Tiles (Section 6)
  if (document.getElementById('chart-scope1-heat')) {
    const allActivities = [];
    Object.values(MIDOR_DATA.scope1.categories).forEach(cat => {
      allActivities.push(...cat.activities);
    });
    makeHeatTiles('chart-scope1-heat', allActivities, 'All Sources');
  }

  // Scope 1 Gas Split (Section 6)
  if (document.getElementById('chart-scope1-gas')) {
    makeGasSplit('chart-scope1-gas');
  }

  // Scope 2 Supplier Split (Section 7)
  if (document.getElementById('chart-scope2-suppliers')) {
    makeSupplierSplit('chart-scope2-suppliers', MIDOR_DATA.scope2.suppliers);
  }

  // Scope 3 Waterfall (Section 8)
  if (document.getElementById('chart-scope3-products')) {
    const products = MIDOR_DATA.scope3.categories['Use of Sold Products (Cat 11)'].products;
    makeWaterfall('chart-scope3-products', products);
  }

  // Intensity KPIs (Section 9)
  if (document.getElementById('chart-intensity-crude')) {
    makeSparkKPI(
      'chart-intensity-crude',
      MIDOR_DATA.intensities.tCO2e_per_kton_crude,
      'tCO₂e / kton crude',
      'Carbon Intensity (Crude)'
    );
  }

  if (document.getElementById('chart-intensity-fired')) {
    makeSparkKPI(
      'chart-intensity-fired',
      MIDOR_DATA.intensities.tCO2e_per_GJ_fired,
      'tCO₂e / GJ',
      'Carbon Intensity (Fired Duty)'
    );
  }

  // Roadmap Timeline (Section 12)
  if (document.getElementById('roadmap-container')) {
    makeRoadmapTimeline('roadmap-container');
  }
}

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeAllCharts);
} else {
  initializeAllCharts();
}
