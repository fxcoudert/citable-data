#include <iostream>
#include <chemfiles.hpp>
#include <iomanip>

using namespace std;
using namespace chemfiles;

#define PI 3.14159265

int main() {
	
	// Load file
    Trajectory file("../../Equilibration_zeolites_defect/MFI_4.00_strong_defect_per_cell/Movies/System_0/Framework_final.pdb");

	// Read frame.
    auto frame = file.read();
    
    // Access atom positions
    auto positions = frame.positions();

	// store name atoms
	vector<string> name(frame.size()," ");
	
	for(int i = 0; i<frame.size(); i++)
		name[i] = frame[i].name();

	//Output the new structure of MFI with default nest.
	auto frame_new = chemfiles::Frame(chemfiles::UnitCell({40.140, 19.920, 26.840} , {90.00, 90.00, 90.00}));
	
	
    for(int j = 0; j < frame.size(); j++)
    {					
		frame_new.add_atom(chemfiles::Atom(name[j]), {positions[j][0], positions[j][1], positions[j][2]});	
	}
			
	auto trajectory_new = chemfiles::Trajectory("MFI_Olson_SI_defect_4.00_per_cell_equilibrated.cif", 'w');
    trajectory_new.write(frame_new);

    return 0;
}

