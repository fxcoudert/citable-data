#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
#include <vector>
#include <math.h>
#include <sstream>

using namespace std;

#define KT 2.494338785 // in kJ/mol
#define SQR(x) x*x

double Error(vector<double> my_vector, double average);

int main(void) 
{
    int number_file = 1; 
    
	vector<string> files(number_file,"");
	
	stringstream ss;
	
	// declare file
	for(int i=1; i<=number_file; i++)
	{
		ss << i;
		files[i-1] = "NCMC_chemical_potential_water/AlchemicalWork.txt";
		ss.str("");
	}
	
	ifstream iFS;
	
	vector<int> lines(number_file,0);
	
	string buffer;
	
	// Load the trajectory and count lines	
	for(int i = 0; i < number_file; i++)
	{
		iFS.open(files[i].c_str());
		if(iFS)
		{
			while(getline(iFS, buffer))
			{
				lines[i]++;
			}
		}
		else
		{
			cout << "Cannot open file " << files[i] << endl;
		}
		
		lines[i]--; // remove the first line (which is text).
	
		iFS.close();
		iFS.clear();
	}
	
	double number_1;
	double number_2;
	double number_3;
	double number_4;
	double number_5;
	double number_6;
	double number_7;
	
	vector<double> W;
	vector<double> W_elec;
	vector<double> W_vdw;
	
	// Store quantity
	for(int i = 0; i < number_file; i++)
	{
		iFS.open(files[i].c_str());
		if(iFS)
		{
			getline(iFS, buffer);
			for(int j = 0; j < lines[i]; j++)
			{
				iFS >> number_1 >> number_2 >> number_3 >> number_4 >> number_5 >> number_6 >> number_7;
				W.push_back(number_3);
				W_elec.push_back(number_5);
				W_vdw.push_back(number_7);
			}
		}
		else
		{
			cout << "Cannot open file " << files[i] << endl;;
		}
	
		iFS.close();
		iFS.clear();
	}

	//---------------------------------//
		// Compute of Alchemical work
	//---------------------------------//
	
	W.resize(3001);
	W_elec.resize(3001);
	W_vdw.resize(3001);
	
	// calculate average of W
	double average_W = 0;
	double average_W_elec = 0;
	double average_W_vdw = 0;
	
	for(int i = 0; i < W.size(); i++)
	{
		average_W += W[i];
		average_W_elec += W_elec[i];
		average_W_vdw += W_vdw[i];
	}
	
	average_W /= W.size();
	average_W_elec /= W_elec.size();
	average_W_vdw /= W_vdw.size();
	
	// Calculate error of W
	double error_W=0;
	error_W=Error(W,average_W);
	
	double error_W_elec=0;
	error_W_elec=Error(W_elec,average_W_elec);

	double error_W_vdw=0;
	error_W_vdw=Error(W_vdw,average_W_vdw);

	//---------------------------------//
			// Compute of mu.
	//---------------------------------//
	
	double average_mu = 0;
	double average_exp_W = 0;
	vector<double> exp_W(W.size(),0.0);
	
	for(int i = 0; i < W.size(); i++)
	{
		exp_W[i] = exp(-W[i]/KT);
		average_exp_W += exp_W[i];
	}
		
	average_exp_W /= exp_W.size();	
	
	// Calculate error of W
	double error_exp_W=0;
	double error_mu=0;
	
	error_exp_W=Error(exp_W,average_exp_W);
	
	average_mu = -KT*log(average_exp_W);
	error_mu = KT*error_exp_W/average_exp_W;
    
    cout << "elec" << average_W_elec << " " << error_W_elec << endl;
	cout << "vdw" << average_W_vdw << " " << error_W_vdw << endl;

	// Output file.

	string output = "Results_osmostat_insertion_2_water.txt";

	ofstream oFS;
	
	oFS.open(output.c_str());
	
	if(oFS)
	{
		oFS << "osmostat: vacuum -> 2*H20 (300K): Number of pseudo widom attemps: \t";
		oFS << W.size();
		oFS << ". " << endl;
		oFS << "Average Alchemical Work :\t\t\t\t\t\t\t" << average_W << " +/- " << error_W << " kJ/mol." << endl;
		oFS << "Chemical potential (divided by 2 for one water) :\t\t\t\t\t\t\t" << average_mu/2 << " +/- " << error_mu/2 << " kJ/mol." << endl;
		oFS << "Chemical potential (divided by 2 for one water) :\t\t\t\t\t\t\t" << (average_mu/2)/4.184 << " +/- " << (error_mu/2)/4.184 << " kcal/mol." << endl;
	}
	else
	{
		cout << "Cannot open file." << endl;
	}
	
	oFS.close();
	oFS.clear();

    output = "Alchemical_work_insertion_2_water.txt";

    oFS.open(output.c_str());

    if(oFS)
    {
        oFS << "#Alchemical Work (kJ/mol)   electrostatic_part (kJ/mol)		vdw_part (kJ/mol)" << endl;
        for(int i = 0; i < W.size(); i++)
            oFS << i << " " << W[i] << " " << W_elec[i] << " " << W_vdw[i] << endl;
	}
    else
    {
        cout << "Cannot open file." << endl;
    }

    oFS.close();
    oFS.clear();
	
    return 0;
}

double Error(vector<double> my_vector, double average_total)
{
	int NR_BLOCKS = 5;
	
	int new_size = floor(my_vector.size()/NR_BLOCKS);
	
	vector<double> average_blocks(NR_BLOCKS,0.0);
	
	double sum_sqr=0.0;
	double sum = 0.0;
	
	for(int i = 0; i < NR_BLOCKS; i++)
	{
		for(int j = 0; j < new_size; j++)
		{
            //cout << i*new_size+j << endl;
			average_blocks[i] += my_vector[i*new_size+j];
		}
        //cout << endl;
		average_blocks[i] /= new_size;
		//cout << average_blocks[i] << "	" << average_total <<endl;
	}
	
	double error=0;
	
	// Error calculation
	for(int i = 0; i < NR_BLOCKS; i++)
		error += (average_blocks[i]-average_total)*(average_blocks[i]-average_total);
	
	error = sqrt(error/(NR_BLOCKS-1));
	
	return error;
}
