Wnls_fw = read(get_absolute_file_path("Epsilon.sce") + "..\Data\FwWnls.txt", 10, 1);

Wnls_rv = read(get_absolute_file_path("Epsilon.sce") + "..\Data\RvWnls.txt", 10,1);


plot2d(Wnls_fw,flipdim(fwData(:, 1),1), 2);


ke1 = lsq(Wnls_fw, flipdim(fwData(:, 1),1))

ke2 = lsq(Wnls_rv, rvData(:,1))

ke = (ke1+ke2) * 0.5


km = ke


L = 0.0047
plot2d(Wnls_fw, ke*Wnls_fw, 5)




