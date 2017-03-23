 function [centers, rads] = sampleSpheres( dims, n ) 
 % main function which is to be called for adding multiple spheres in a cube
 % dims is assumed to be a row vector of size 1-by-ndim
 % For demo take dims = [ 2 2 2 ] and n = 50 

 % preallocate
 ndim = numel(dims);
 centers = zeros( n, ndim );
 rads = zeros( n, 1 );
 ii = 1;
 while ii <= n
      [centers(ii,:), rads(ii) ] = randomSphere( dims );     
      if nonOver( centers(1:ii,:), rads(1:ii) )
           ii = ii + 1; % accept and move on
      end
 end