export default function AuthLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <>
      <main className="flex items-center justify-center w-full py-2">
        {children}
      </main>
    </>
  );
}