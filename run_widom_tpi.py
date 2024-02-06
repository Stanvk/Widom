import matplotlib.pyplot as plt
import numpy as np
from Helpers.Container import Container
import MDAnalysis as md
from datetime import datetime
from Widom.Widom import Widom
from Widom.Dioxygen import Dioxygen
from Helpers.Plotter import Plotter

basepath = '/Users/stanvk/Projects/NTUA/systems/pe_configurations_298K/'
relative_outputpath = 'Analysis/Widom/'

config = Container(basepath, relative_outputpath).load(filename='')

sample = md.Universe(basepath+config.get('topology_file'), basepath+config.get('coordinate_file'))

config.set('frame_series', np.arange(0,len(sample.trajectory),1).tolist())
config.save(filename='config_'+config.get_timestamp())

tpi = Widom(Dioxygen())
tpi.set_sample(sample, config.get('LJ_params_solvent'))

tpi.prepare(frame=config.get('frame'), number_of_insertions=config.get('n_insertions'))
tpi.run()

Plotter()

tpi.save_LJ_energies(config.output_path, config.get_timestamp())

plt.hist(tpi.get_LJ_energies())
plt.xlabel(r'$\mathrm{Insertion}$ $\mathrm{energy}$ [$\mathrm{kJ} \mathrm{mol}^{-1}$]')
plt.ylabel(r'$\mathrm{Frequency}$')
plt.savefig(config.output_path+'LJ_energies_histogram_'+config.get_timestamp()+'.pdf', format='pdf', bbox_inches='tight')
plt.close()

plt.plot(range(1,tpi.number_of_insertions), tpi.calculate_moving_solubility(config.get('temperature'), tpi.get_LJ_energies()))
plt.ylabel(r'$\langle \exp(-\beta \Delta E)\rangle_N$')
plt.xlabel(r'Iteration number $N$')
plt.savefig(config.output_path+'solubility_'+config.get_timestamp()+'.pdf', format='pdf', bbox_inches='tight')
