using Xunit;

namespace BabylonGameEngine.Tests
{
    public class UserTests
    {
        [Fact]
        public void TestUserCreation()
        {
            // Arrange
            var expectedName = "TestUser";

            // Act
            var user = new User { Name = expectedName };

            // Assert
            Assert.Equal(expectedName, user.Name);
        }
    }
}
