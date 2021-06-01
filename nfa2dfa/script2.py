from automata.fa.nfa import NFA
from automata.fa.dfa import DFA

"""
state	0	1		
s0	{s0	s1}	s3	
s1	s0	{s1	s3}	
s2		{s0	s2}	
s3	{s0	s1	s2}	s1
"""

nfa = NFA(
    states={'s0', 's1', 's2', 's3'},
    input_symbols={'0', '1'},
    transitions={
        's0': {'0': {'s0','s1'}, '1': {'s3'}},
        's1': {'0': {'s0','s1'}, '1': {'s3'}},
        's2': {'1': {'s0','s2'}},
        's3': {'0': {'s0','s1','s2'}, '1': {'s1'}},
    },
    initial_state='s0',
    final_states={'s3'}
)

"""
Test
Expected Output : 
state - 0	1
s0 - s0s1	s3
s0s1 - s0s1	s1s3
s3	- s0s1s2	s1
s1s3 -	s0s1s2	s1s3
s0s1s2	- s0s1	s0s1s2s3
s1	- s0	s1s3
s0s1s2s3	- s0s1s2	s0s1s2s3

Generated Output : 
{'{s0}': {'0': '{s0,s1}', '1': '{s3}'}, 
'{s0,s1}': {'0': '{s0,s1}', '1': '{s3}'}, 
'{s3}': {'0': '{s0,s1,s2}', '1': '{s1}'}, 
'{s0,s1,s2}': {'0': '{s0,s1}', '1': '{s0,s2,s3}'}, 
'{s1}': {'0': '{s0,s1}', '1': '{s3}'}, 
'{s0,s2,s3}': {'0': '{s0,s1,s2}', '1': '{s0,s1,s2,s3}'}, 
'{s0,s1,s2,s3}': {'0': '{s0,s1,s2}', '1': '{s0,s1,s2,s3}'}}
"""

dfa = DFA.from_nfa(nfa)
print(dfa.states)
print(dfa.transitions)