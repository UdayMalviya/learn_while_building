// Payload: Define structure

type Payload struct {
	User struct {
		ID       int64
		Name     string
		Metadata map[string]string
	}
	Items []struct {
		ID    int64
		Price float64
		Tags  []string
	}
	Context struct {
		Timestamp int64
		Flags     []string
	}
}