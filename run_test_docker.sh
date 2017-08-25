docker-compose -f docker-compose.test.yml down
docker-compose -f docker-compose.test.yml up --build -d

echo "Waiting until container becomes healthy..."

retries=0
while ! docker ps | grep lightweightresttester_json-server | grep healthy; do
    sleep 1

    if [ "$retries" -gt 10 ]
    then
        break
    fi

    retries=$(($retries+1))
done

if [ "$retries" -gt 10 ]
then
    echo "Fail!"
else
    echo "Done!"
fi

tox
