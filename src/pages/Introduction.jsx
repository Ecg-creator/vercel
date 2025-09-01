import React from 'react';
import { Link } from 'react-router-dom';

const Introduction = () => {
  return (
    <div className="max-w-4xl mx-auto">
      <section className="mb-10">
        <h1 className="text-4xl font-bold mb-4">Welcome to Empire OS</h1>
        <p className="text-xl text-gray-400">
          The unified digital governance platform where structure creates value, roles drive efficiency, 
          and commerce flows in harmony across the Virtual Silk Road.
        </p>
      </section>
      
      <section className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
        <div className="bg-gray-800 p-6 rounded-lg">
          <h2 className="text-2xl font-bold mb-3 text-amber-400">Ecosystem Overview</h2>
          <p className="mb-4">Empire OS is a modular governance platform that orchestrates business interactions, 
          licensing, identity, and commerce across interconnected marketplaces to maximize profit potential and operational efficiency.</p>
          <Link to="/dashboard" className="text-blue-400 hover:underline">Explore Dashboard →</Link>
        </div>
        
        <div className="bg-gray-800 p-6 rounded-lg">
          <h2 className="text-2xl font-bold mb-3 text-green-500">Governance Structure</h2>
          <p className="mb-4">Our digital economy is governed through Empire OS, administered by ECG, 
          licensed via Synergyze, with identities secured through DigitalMe — creating a seamless ecosystem for revenue generation.</p>
          <Link to="/ecg-council" className="text-blue-400 hover:underline">Learn about Governance →</Link>
        </div>
      </section>
      
      <section className="mb-12">
        <h2 className="text-2xl font-bold mb-6">Core Modules</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <ModuleCard 
            title="Synergyze" 
            description="Where businesses are born and powered. Register companies, manage licenses, and access modules to unlock new revenue streams." 
            color="amber-400"
            link="/synnergyze"
          />
          <ModuleCard 
            title="DigitalMe" 
            description="Your Digital DNA across the Empire. Manage identity, roles, and access controls for optimized business operations." 
            color="blue-500"
            link="/digitalme"
          />
          <ModuleCard 
            title="Woven Supply" 
            description="The pre-retail marketplace where manufacturing meets demand, driving efficient production and maximizing supplier margins." 
            color="sky-400"
            link="/woven-supply"
          />
          <ModuleCard 
            title="Commune Connect" 
            description="The gateway to consumer engagement. Connect brands to buyers and optimize retail channels for maximum ROI." 
            color="amber-500"
            link="/commune-connect"
          />
          <ModuleCard 
            title="ECG Council" 
            description="Ministry of Internal Affairs + External Partner Enablement, overseeing profit-sharing models and commission structures." 
            color="green-500"
            link="/ecg-council"
          />
          <ModuleCard 
            title="Emperor View" 
            description="Full visibility of the Silk Road with aggregated performance analytics for strategic decision-making and profit monitoring." 
            color="purple-500"
            link="/emperor-view"
          />
        </div>
      </section>
      
      <section className="bg-gray-800 p-8 rounded-lg mb-10">
        <h2 className="text-2xl font-bold mb-4">Profit Maximization Framework</h2>
        <p className="mb-6">Empire OS is designed to optimize every transaction within your digital commerce ecosystem:</p>
        <ul className="list-disc pl-6 space-y-3">
          <li>Modular licensing structure ensures targeted revenue streams from each business function</li>
          <li>Integrated marketplaces reduce friction and increase transaction volume</li>
          <li>Governance mechanisms protect value and enforce profitable trade relationships</li>
          <li>Robust analytics enable data-driven optimization of your entire business network</li>
          <li>Automated compliance reduces operational costs while maintaining regulatory standards</li>
        </ul>
        <div className="mt-6">
          <Link to="/dashboard" className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
            Begin Maximizing Value
          </Link>
        </div>
      </section>
      
      <section className="mb-10">
        <h2 className="text-2xl font-bold mb-4">Getting Started</h2>
        <p className="mb-6">New to Empire OS? Follow these steps to begin your journey toward optimized business operations:</p>
        <ol className="list-decimal pl-6 space-y-3">
          <li>Register your business through Synergyze</li>
          <li>Create your DigitalMe identity profile</li>
          <li>Apply for appropriate licenses for your business type</li>
          <li>Connect to either Woven Supply (manufacturing) or Commune Connect (retail)</li>
          <li>Begin transactions on the Virtual Silk Road</li>
        </ol>
      </section>
    </div>
  );
};

const ModuleCard = ({ title, description, color, link }) => (
  <div className={`bg-gray-800 p-4 rounded-lg border-l-4 border-${color}`}> 
    <h3 className={`text-xl font-bold mb-2 text-${color}`}>{title}</h3>
    <p className="mb-3 text-sm">{description}</p>
    <Link to={link} className="text-blue-400 text-sm hover:underline">Explore Module →</Link>
  </div>
);

export default Introduction;