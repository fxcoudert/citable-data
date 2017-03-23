 function [ c r ] = randomSphere( dims )
 % creating one sphere at random inside [0..dims(1)]x[0..dims(2)]x...
 % In general cube dimension would be 10mm*10mm*10mm
 % radius and center coordinates are sampled from a uniform distribution 
 % over the relevant domain.
 %
 % output: c - center of sphere (vector cx, cy,... )
 %         r - radius of sphere (scalar)
 %r = 5E-6 + ( 8E-6 - 5E-6) .* rand(1);% radius varies between 0.15mm - 0.55mm
 r = 2.0E-5;
 c = bsxfun(@times,(dims - 2*r) , rand(1,3)) + r; % to make sure sphere is placed inside the cube
