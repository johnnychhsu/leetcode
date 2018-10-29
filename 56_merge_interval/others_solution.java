public List<Interval> merge(List<Interval> intervals) {
        if (intervals == null || intervals.size() <= 1) return intervals;
        PriorityQueue<Interval> queue = new PriorityQueue<>((a,b) -> a.start-b.start);
        List<Interval> result = new ArrayList<>();
        for (Interval v : intervals) queue.offer(v);
        Interval prev = queue.poll();
        while (!queue.isEmpty()) {
            while(!queue.isEmpty()&&prev.end>=queue.peek().start){ //whenever the current interval's start is smaller than the previous one's end, pop it out
                prev.end = Math.max(prev.end, queue.poll().end); //here remember to save the biggest end value to prev
            }
            result.add(new Interval(prev.start, prev.end));
            if(!queue.isEmpty()){
                prev = queue.poll();
                if(queue.isEmpty()) result.add(prev); //add the last one in priorityqueue
            } 
        }
        return result;
    }
