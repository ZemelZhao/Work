class RecentCounter{
	Queue<Integer> cache;
	public RecentCounter(){
		cache = new LinkedList<Integer> ();
	}
	public int ping(int t){
		cache.add(t);
		while(cache.peek()+3000 < t){
			cache.poll();
		}
		return cache.size();
	}
}
