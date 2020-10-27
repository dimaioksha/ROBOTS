plot2d(simulation.time, simulation.values, 5);

fprintfMat(get_absolute_file_path("DrawSimulation.sce") + "..\Data\Sim" + currIdx + ".txt",[simulation.values simulation.time], "%.5f");

fprintfMat(get_absolute_file_path("DrawSimulation.sce") + "..\Data\Model" + currIdx + ".txt", [model time], "%.5f");
