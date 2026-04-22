import Veil

set_option linter.dupNamespace false

veil module MyMutex

type node
type ticket

instantiate tot : TotalOrder node

enum state = {idle, waiting, critical}
-- Nodes
relation critical : node → Prop
function choosing : node → Prop
function number   : node → ℕ
function cs : node → state

#gen_state

#print State

after_init {
  critical N := False;
  choosing N := False;
  number N := 0;
  cs N  := idle;
}

#print initialState?


action choose (n : node)  = {
  require ¬ choosing n;
  choosing n := True;

  -- Find ticket value greater than all others
  let t_max ← fresh;
  require ∀ j, j ≠ n → number j < t_max;
  number n := t_max;

  choosing n := False;
}

action enter (n : node) = {
  require number n != 0;

  require ∀ j, j ≠ n →
    (¬ choosing j) ∧ ((number j = 0) ∨ (number n < number j) ∨ (number n = number j ∧ tot.le n j));

  critical n := True;
}

action exit (n : node) = {
  require critical n
  number n := 0
  critical n := False
}


safety [mutex] critical I ∧ critical J → I = J


#gen_spec
#check_invariants

end MyMutex
