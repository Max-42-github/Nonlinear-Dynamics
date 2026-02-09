function out = Ddd(D, M, S)
%--------------------------------------------------------------------------
%
% Ddd: Conversion of angular degrees, minutes and seconds of arc to decimal
%      representation of an angle 
%
% Inputs:
%   D        Angular degrees
%   M        Minutes of arc
%   S        Seconds of arc
%
% Output:
%   out      Angle in decimal representation
%
% Last modified:   2015/08/12   M. Mahooti
%
%--------------------------------------------------------------------------

if ( (D<0) || (M<0) || (S<0) )
    sign = -1;
else
    sign = 1;
end

out = sign*(abs(D)+abs(M)/60+abs(S)/3600);

