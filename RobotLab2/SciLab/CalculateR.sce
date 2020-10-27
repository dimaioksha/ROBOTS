Rfw = 0
Rrv = 0

fw1 = 0;
rv1 = 0;
fw2 = 0;
rv2 = 0;
for i = 1:10
    fw1 = fw1 + fwData(i, 1) * fwData(i, 2);
    fw2 = fw2 + fwData(i, 2) * fwData(i, 2);

    rv1 = rv1 + rvData(i, 1) * rvData(i, 2);
    rv2 = rv2 + rvData(i, 2) * rvData(i, 2);
end

Rfw = fw1/fw2
Rrv = rv1/rv2

R = (Rfw + Rrv) * 0.5
