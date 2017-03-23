for i= [1 10 50 100 200 300 400]
for k = [0]


%model = mphload('MMM.mph');
%
%model.geom.create('geom1', 3);
% geomtag = 'geom1';


MMMdim = [400E-6 400E-6 100E-6]

Nparticles = i

[c, r] = sampleSpheres(MMMdim, Nparticles);

volumeMem = MMMdim(1,1)*MMMdim(1,2)*MMMdim(1,3);

volumeParticles = sum((4/3)*pi*r.^3);

MMMperc = volumeParticles/volumeMem * 100
%
% %
% %create mat properties (to add)
%
% model.material.create('mat1', 'Common', 'mod1');
% model.material('mat1').label('ZIF8');
% model.material('mat1').propertyGroup('def').set('density', '924.3010');
% model.material('mat1').propertyGroup('def').set('youngsmodulus', '2.953E9');
% model.material('mat1').propertyGroup('def').set('poissonsratio', '0.33');
%
% model.material.create('mat2', 'Common', 'mod1');
% model.material('mat2').label('Polysilicon');
% model.material('mat2').propertyGroup('def').set('density', '242[kg/m^3]');
% model.material('mat2').propertyGroup('def').set('poissonsratio', '0.3');
% model.material('mat2').propertyGroup('def').set('youngsmodulus', '1e10[Pa]');
%
%
% %create system
%
% model.geom('geom1').create('blk1', 'Block');
% model.geom('geom1').feature('blk1').set('size', [MMMdim(1,1) MMMdim(1,2) MMMdim(1,3)]);
% %model.material('mat2').selection.set([1]);
%
%
%
%
% for n = 1:Nparticles
%     name = ['sph' num2str(n)];
%     model.geom(geomtag).create(name, 'Sphere');
%     model.geom(geomtag).feature(name).set('r', r(n));
%     model.geom(geomtag).feature(name).set('pos', [ c(n,1) c(n,2) c(n,3) ]);
%     %model.material('mat1').selection.set(n+1);
% end
%
% model.geom('geom1').run;
% model.material('mat2').selection.set([1]);
% model.material('mat1').selection.set([2:Nparticles+1]);
%
%  %create study
%
% model.study.create('std1');
% model.study('std1').create('stat', 'Stationary');
% model.physics.create('solid', 'SolidMechanics', 'geom1');
% model.study('std1').feature('stat').activate('solid', true);
% model.study('std1').feature('stat').set('geometricNonlinearity', 'on');
%
% model.param.set('stress', '0.1 [GPa]');
% model.physics('solid').feature('lemm1').feature.create('iss1', 'InitialStressandStrain', 3);
% model.physics('solid').feature('lemm1').feature('iss1').selection.set([2:Nparticles+1]);
% model.physics('solid').feature('lemm1').feature('iss1').label('-');
% model.physics('solid').feature('lemm1').feature('iss1').label('AdsorptiveStress');
% model.physics('solid').feature('lemm1').feature('iss1').set('Sil', {'stress' '0' '0' '0' 'stress' '0' '0' '0' 'stress'});
%
% ModelUtil.showProgress(true)
% model.mesh.create('mesh1', 'geom1');
% %model.mesh('mesh1').autoMeshSize(2);
% model.mesh('mesh1').run;
%
% model.physics('solid').feature.create('fix1', 'Fixed', 0);
% model.physics('solid').feature('fix1').selection.set([1]);
%
% model.sol.create('sol1');
% model.sol('sol1').study('std1');
%
% model.sol('sol1').create('st1', 'StudyStep');
% model.sol('sol1').feature('st1').set('study', 'std1');
% model.sol('sol1').feature('st1').set('studystep', 'stat');
% model.sol('sol1').create('v1', 'Variables');
% model.sol('sol1').feature('v1').set('control', 'stat');
% model.sol('sol1').feature('v1').set('scalemethod', 'init');
% model.sol('sol1').create('s1', 'Stationary');
% model.sol('sol1').feature('s1').create('fc1', 'FullyCoupled');
% model.sol('sol1').feature('s1').feature('fc1').set('termonres', 'auto');
% model.sol('sol1').feature('s1').feature('fc1').set('reserrfact', 1000);
% model.sol('sol1').feature('s1').feature('fc1').set('linsolver', 'dDef');
% model.sol('sol1').feature('s1').feature('fc1').set('termonres', 'auto');
% model.sol('sol1').feature('s1').feature('fc1').set('reserrfact', 1000);
% model.sol('sol1').feature('s1').feature.remove('fcDef');
% model.sol('sol1').attach('std1');
%
% model.study('std1').create('param', 'Parametric');
% model.study('std1').feature('param').set('sweeptype', 'sparse');
% model.study('std1').feature('param').setIndex('pname', 'stress', 0);
% model.study('std1').feature('param').setIndex('plistarr', '', 0);
% model.study('std1').feature('param').setIndex('punit', '', 0);
% model.study('std1').feature('param').setIndex('pname', 'stress', 0);
% model.study('std1').feature('param').setIndex('plistarr', '', 0);
% model.study('std1').feature('param').setIndex('punit', '', 0);
% model.study('std1').feature('param').setIndex('plistarr', 'range(0,0.1,1)', 0);
% model.study('std1').feature('param').setIndex('punit', 'GPa', 0);
%
% model.sol('sol1').runAll;
%
% model.result.numerical.create('av1', 'AvVolume');
% model.result.numerical('av1').selection.all;
% model.result.numerical('av1').selection.set([2:Nparticles+1]);
% model.result.numerical('av1').set('expr', 'solid.evol');
model.result.table.create('tbl1', 'Table');
model.result.table('tbl1').comments('Volume Average 1 (solid.evol)');
model.result.numerical('av1').set('table', 'tbl1');
model.result.numerical('av1').setResult;


filename = sprintf('MMM_%d_%d.mph', Nparticles, k);


mphsave(model,filename)

end

end
