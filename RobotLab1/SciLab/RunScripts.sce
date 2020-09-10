pathname = get_absolute_file_path("RunScripts.sce");

exec(pathname + 'LoadData.sce', -1);
exec(pathname + 'MakeModel.sce', -1);
xcos(pathname + 'Simulation.zcos');
//exec(pathname + 'DrawSimulation.sce', -1);
