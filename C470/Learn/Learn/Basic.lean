import Veil

set_option linter.dupNamespace false

veil module MyMutex

type node

instantiate tot : TotalOrder node

-- Nodes
relation critical : node → Prop
function choosing : node → Prop
function number   : node → Prop
enum state = {idle, waiting, critical}

function cs : node → state
function t : node → ℕ
function serving : node → ℕ



#gen_state


#print State

after_init {
  critical N := False;
  choosing N := False;
  number N := False;
  serving N := 0;
  cs N := idle;
  t N := 0;

}

#print initialState?

action choose (n : node)  = {
  require ¬ choosing n ;
  choosing n := True;
  number n := True;
}

action exit (n : node) = {
  require critical n;
  critical n := False;

}



end MyMutex
