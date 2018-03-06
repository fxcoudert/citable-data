(*
Copyright (c) 2016 F.X. Coudert & G. Fraux

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*)

BeginPackage[ "OFAST`"]

(* Solve the IAST equations for Langmuir isotherms *)
IASTLangmuir[KB_, NB_, KC_, NC_, yB_, P_] := Module[{yC, xB, xC, alpha, PBs, PCs, Ntot, NBs, NCs},
    yC = 1 - yB;
    PBs = PBs /. FindRoot[
        P * yC * PBs / (PBs - P * yB) == 1 / KC *((1 + KB * PBs)^(NB / NC)- 1),
        {PBs, P * yB * 1.001}];
    xB = P * yB / PBs;
    xC = 1 - xB;
    alpha =(xB / xC)/(yB / yC);
    PCs = P * yC / xC;
    NBs = NB * KB * PBs /(1 + KB * PBs);
    NCs = NC * KC * PCs /(1 + KC * PCs);
    Ntot = 1 /(xB / NBs + xC / NCs);
    Return[{alpha, xB, Ntot}];
]

(* Solve the IAST equations for linear isotherms *)
IASTLinear[thetaB_, thetaC_, yB_, P_] := Module[{yC, xB, xC, alpha, PBs, PCs, NBs, NCs, Ntot},
    yC = 1 - yB;
    PBs = P *(yB + yC * thetaC / thetaB);
    xB = P * yB / PBs;
    xC = 1 - xB;
    alpha =(xB / xC)/(yB / yC);
    PCs = P * yC / xC;
    NBs = thetaB * PBs;
    NCs = thetaC * PCs;
    Ntot = 1 /(xB / NBs + xC / NCs);
    Return[{alpha, xB, Ntot}];
]

(* Calculate DeltaOmega between the two phases, using IAST *)
(* ==== For linear + langmuir isotherms *)
DeltaOmega[thetaB1_, thetaC1_, KB2_, NB2_, KC2_, NC2_, DeltaF_, yB_, P_?NumericQ] :=
Module[{Ndiff, pp, R, T},
    Ndiff[pp_?NumericQ] := (IASTLinear[thetaB1, thetaC1, pp][[3]]
                          - IASTLangmuir[KB2, NB2, KC2, NC2, yB, pp][[3]]);
    R = 8.314;
    T = 298;
    Return[DeltaF - R * T * NIntegrate[Ndiff[pp]/ pp, {pp, 0, P}]];
]

(* ==== For two langmuir isotherms *)
DeltaOmega[KB1_, NB1_, KC1_, NC1_, KB2_, NB2_, KC2_, NC2_, DeltaF_, yB_, P_?NumericQ] :=
Module[{Ndiff, pp, R, T},
    Ndiff[pp_?NumericQ] := (IASTLangmuir[KB1, NB1, KC1, NC1, yB, pp][[3]]
                          - IASTLangmuir[KB2, NB2, KC2, NC2, yB, pp][[3]]);
    R = 8.314;
    T = 298;
    Return[DeltaF - R * T * NIntegrate[Ndiff[pp]/ pp, {pp, 0, P}]];
]

(* ==== For null + langmuir isotherms *)
DeltaOmega[KB_, NB_, KC_, NC_, DeltaF_, yB_, P_?NumericQ] := Module[{Ndiff, pp, R, T},
    Ndiff[pp_?NumericQ] := - IASTLangmuir[KB, NB, KC, NC, yB, pp][[3]];
    R = 8.314;
    T = 298;
    Return[DeltaF - R * T * NIntegrate[Ndiff[pp]/ pp, {pp, 0, P}]];
]

(* Full solution of the OFAST equations, using DeltaOmega to choose the most stable phase *)
(* ==== For linear + langmuir isotherms *)
SolveOFAST[thetaB1_, thetaC1_, KB2_, NB2_, KC2_, NC2_, DeltaF_, yB_, P_] :=
Module[{Ntot, dOmega, alpha, xB},
    dOmega = DeltaOmega[thetaB1, thetaC1, KB2, NB2, KC2, NC2, DeltaF, yB, P];
    If[dOmega < 0,
        {alpha, xB, Ntot} = IASTLinear[thetaB1, thetaC1, yB, P],
        {alpha, xB, Ntot} = IASTLangmuir[KB2, NB2, KC2, NC2, yB, P]
    ];
    Return[{alpha, Ntot, xB, dOmega}];
]
(* ==== For two langmuir isotherms *)
SolveOFAST[KB1_, NB1_, KC1_, NC1_, KB2_, NB2_, KC2_, NC2_, DeltaF_, yB_, P_] :=
Module[{Ntot, dOmega, alpha, xB},
    dOmega = DeltaOmega[KB1, NB1, KC1, NC1, KB2, NB2, KC2, NC2, DeltaF, yB, P];
    If[dOmega < 0,
        {alpha, xB, Ntot} = IASTLangmuir[KB1, NB1, KC1, NC1, yB, P],
        {alpha, xB, Ntot} = IASTLangmuir[KB2, NB2, KC2, NC2, yB, P]
    ];
    Return[{alpha, Ntot, xB, dOmega}];
]
(* ==== For null + langmuir isotherms *)
SolveOFAST[KB_, NB_, KC_, NC_, DeltaF_, yB_, P_] := Module[{Ntot, dOmega, alpha, xB},
    dOmega = DeltaOmega[KB, NB, KC, NC, DeltaF, yB, P];
    If[dOmega < 0,
        {alpha, xB, Ntot} = {0, 0, 0},
        {alpha, xB, Ntot} = IASTLangmuir[KB, NB, KC, NC, yB, P]
    ];
    Return[{alpha, Ntot, xB, dOmega}];
]

EndPackage[]
