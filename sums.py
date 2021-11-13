
sides = [1, 2, 3, 4, 5, 6]
tops = [1, 2, 3, 4, 5, 6]  # We don't need 4, 5, or 6, because the 7s complements are the same


class Die(object):
	def __init__(self, right, left):
		self.right = right
		self.left  = left


class ThreeDSix(object):
	def __init__(self, d1, d2, d3):
		self.d1 = d1
		self.d2 = d2
		self.d3 = d3

	def TwoDSix(self):
		return (
			6 - ((self.d1.right + self.d2.right + self.d3.right) % 6),
			6 - ((self.d1.left  + self.d2.left  + self.d3.left ) % 6),
		)

	def TwoDSixSum(self):
		return sum(self.TwoDSix())


def side_rolls(top):
	return [side for side in sides if side not in [top, 7 - top]]



rolls = [ThreeDSix(Die(topX, side_rolls(topX)[sideX]),
                   Die(topY, side_rolls(topY)[sideY]),
                   Die(topZ, side_rolls(topZ)[sideZ]))
         for topX in tops
         for topY in tops
         for topZ in tops
         for sideX in range(4)
         for sideY in range(4)
         for sideZ in range(4)]

sums = list(map(ThreeDSix.TwoDSixSum, rolls))
sum_counts = {sum: sums.count(sum) for sum in range(2, 13)}

print()
print("3d6 rolled in a right angle trough, where the left and right sides are treated as")
print("separate d6 rolls, using (6 - (sum % 6)), to get a range from 1 to 6.")
print()
print()
print("Sum comparison")
print()
print("     " + ("{:6} " * 11).format(*range(2, 13))) 
print("3d6: " + "".join(map("{:6.1f}%".format, map(lambda x: (x / len(rolls)) * 100, list(zip(*sum_counts.items()))[1]))))
twoD6_sums = [1, 2, 3, 4, 5, 6, 5, 4, 3 ,2 ,1]
print("2d6: " + "".join("{:6.1f}%".format((twoD6_sums[sum - 2] / 36) * 100)  for sum in range(2, 13)))
print("\n")


print("Roll pair frequency comparison")
print()
print("{:<7}{:>8} {:>8}".format("Pairs", "3d6", "2d6"))
pairs = [(x, y) for x in range(1, 7) for y in range(1, 7)]
threeD6_pairs = [(x, y) for x, y in map(ThreeDSix.TwoDSix, rolls)]
pairs_freq = [(str(pair), threeD6_pairs.count(pair) / len(threeD6_pairs) * 100, 100/36) for pair in pairs]
print("\n".join(map("{0[0]:<7}{0[1]:>8.1f}%{0[2]:>8.1f}%".format, pairs_freq)))












