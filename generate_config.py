from Helpers.Container import Container

basepath = '/Users/stanvk/Projects/NTUA/systems/pe_configurations_298K/'
relative_outputpath = 'Analysis/Widom/'

config = Container(basepath, relative_outputpath)
config.set('basepath', basepath)
config.set('topology_file', 'pe.tpr')
config.set('coordinate_file', 'semicryst.gro')
config.set('relative_outputpath',relative_outputpath)
config.set('temperature', 298)
config.set('n_insertions', int(1e5))
config.set('frame', 0)
config.set('test_particle', 'Dioxygen')
config.set('LJ_params_solvent', {'CH2': [0.38493, 3.950], 'CH3': [0.81588, 3.750]})
# config.set('LJ_params_solvent', {'CH': [0.0828, 4.680], 'CH2': [0.3818, 3.950], 'CH3': [0.8139, 3.750]})

config.save(filename='config_'+config.get_timestamp())