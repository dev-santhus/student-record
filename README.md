# student-record

Python Student Record CRUD API built with FastAPI.

## Run locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

## API endpoints

- `GET /health` - health check
- `POST /students` - create a student
- `GET /students` - list students
- `GET /students/{student_id}` - get one student
- `PUT /students/{student_id}` - update student fields
- `DELETE /students/{student_id}` - delete a student

## Example create payload

```json
{
  "id": 1,
  "name": "Ada Lovelace",
  "age": 20,
  "grade": "A"
}
```