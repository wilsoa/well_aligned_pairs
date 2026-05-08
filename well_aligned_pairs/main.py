#*****************************************************************************
#       Copyright (C) 2026 Alexander N. Wilson <math@alexandernwilson.com>
#
#  Distributed under the terms of the GNU General Public License version 2 (GPLv2)
#
#  The full text of the GPLv2 is available at:
#
#                  http://www.gnu.org/licenses/
#*****************************************************************************

def delta (u):
	from sage.combinat.permutation import Permutation
	return Permutation([x - 1 for x in u if x != 1])

def is_well_aligned (u, v):
	if len(u) != len(v):
		raise TypeError("Permutations must be of the same length to test whether they are well-aligned.")

	if u == v:
		return True

	# Check first that u and v are aligned:
	# (i) the 1 in u must occur weakly left of the 1 in v
	if u.index(1) > v.index(1):
		return False
	# (ii) between the 1 in u and the one in v inclusive, u must increase
	a = u[u.index(1):v.index(1)+1]
	if any(a[i] > a[i + 1] for i in range(len(a) - 1)):
		return False

	# Now that we know (u,v) is aligned, we check
	# that (delta(u), delta(v)) is well-aligned
	return is_well_aligned(delta(u), delta(v))


class WellAlignedPair:
	def __init__ (self, u, v, verify = True):
		r"""
	    A well-aligned pair of permutations..

	    INPUT:

	    - ``u`` -- a permutation.

	    - ``v`` -- a permutation in the same symmetric group as v.

	    - ``verify`` -- boolean or ``None`` (default); whether the
	      pair should be tested for well-alignedness.

	    EXAMPLES::

	        sage: from well_aligned_pairs import WellAlignedPair
	        sage: P.__class__
	        <class 'sage.combinat.posets.posets.FinitePoset_with_category'>

	        sage: Q = sage.combinat.posets.posets.FinitePoset(P, facade = False); Q
	        Finite poset containing 6 elements

	        sage: Q is P
	        True
	    """
		if verify and not is_well_aligned(u, v):
			raise TypeError("Permutations are not well-aligned.")

		self._u = u
		self._v = v

	def __getitem__ (self, i):
		if i == 0:
			return self._u
		if i == 1:
			return self._v
		raise TypeError("A well-aligned pair has only two elements.")

	def __repr__ (self):
		return "╔" + " ".join([str(x) for x in self._u]) + "╗\n╚" + " ".join([str(x) for x in self._v]) + "╝"

def WellAlignedPairs (n, u = None):
	from sage.combinat.permutation import Permutation

	if n == 1:
		yield WellAlignedPair(Permutation([1]), Permutation([1]))
	elif u == None:
		for _u in Permutations(n):
			for pair in WellAlignedPairs(n, _u):
				yield pair
	else:
		min_index = u.index(1)
		max_index = min_index

		# Push max_index as long as u has
		# an ascent
		while max_index < n - 1 and u[max_index] < u[max_index + 1]:
			max_index += 1

		# Every possible v is formed by taking a well-aligned
		# pair with (delta(u),*) with a one placed in each possible
		# index 
		for pair in WellAlignedPairs(n - 1, delta(u)):
			_v = [x + 1 for x in pair[1]]
			for index in range(min_index, max_index + 1):
				yield WellAlignedPair(u, Permutation(_v[0:index] + [1] + _v[index:]))

