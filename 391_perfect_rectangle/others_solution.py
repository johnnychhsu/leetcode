class Solution:
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        res = set()
        min_left = 2 ** 16
        max_right = 0
        max_up = 0
        min_down = 2 ** 16
        
        area = 0
        
        for rec in rectangles:
            l_left = (rec[0], rec[1])
            l_right = (rec[2], rec[1])
            u_left = (rec[0], rec[3])
            u_right = (rec[2], rec[3])
            
            area += (rec[2] - rec[0]) * (rec[3] - rec[1])
            
            min_left = min(min_left, rec[0])
            max_right = max(max_right, rec[2])
            max_up = max(max_up, rec[3])
            min_down = min(min_down, rec[1])
            
            if l_left not in res:
                res.add(l_left)
            else:
                res.remove(l_left)
            
            if l_right not in res:
                res.add(l_right)
            else:
                res.remove(l_right)
                
            if u_left not in res:
                res.add(u_left)
            else:
                res.remove(u_left)
                
            if u_right not in res:
                res.add(u_right)
            else:
                res.remove(u_right)
                
        if len(res) != 4:
            return False
        else:
            total_area = (max_right - min_left) * (max_up - min_down)
            if total_area != area:
                return False
            else:
                upper_right = (max_right, max_up)
                upper_left = (min_left, max_up)
                lower_right = (max_right, min_down)
                lower_left = (min_left, min_down)
                if upper_right not in res or upper_left not in res \
                or lower_right not in res or lower_left not in res:
                    return False
                else:
                    return True
        
        
